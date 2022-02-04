import { prisma } from "../prisma.js";
import { compareSync } from "bcrypt";
import jwt from "jsonwebtoken";

export class AuthService {
  static async login({ correo, password }) {
    const usuarioEncontrado = await prisma.usuario.findUnique({
      where: { correo },
      select: { password: true, tipoUsuario: true, id: true },
      rejectOnNotFound: true,
    });
    const resultado = compareSync(password, usuarioEncontrado.password);
    if (resultado) {
      const token = jwt.sign(
        {
          id: usuarioEncontrado.id,
          mensaje_oculto: "Hola soy un mensaje oculto",
        },
        process.env.JWT_SECRET,
        { expiresIn: "4h" }
      );
      return { message: "Si es el usuario", token };
    } else {
      return { message: "Credenciales incorrectas" };
    }
  }
}
