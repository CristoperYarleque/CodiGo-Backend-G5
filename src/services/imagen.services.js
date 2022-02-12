import { Categoria } from "../models/categorias.model.js";
import fs from "fs";

export class ImagenService {
  static async subirImagen(id, nombreImagen) {
    const categoriaEncontrada = await Categoria.findById(id).catch(
      async (error) => {
        await fs.promises.unlink(nombreImagen);
        throw new Error("Categoria no existe");
      }
    );
    if (!categoriaEncontrada) {
      await fs.promises.unlink(nombreImagen);
      throw new Error("Categoria no existe");
    }
    const categoriaActualizada = await Categoria.findOneAndUpdate(
      { _id: id },
      { categoriaImagen: nombreImagen },
      { new: true }
    );
    return categoriaActualizada;
  }
}
