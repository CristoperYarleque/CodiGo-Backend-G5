import express, { json } from "express";
import mongoose from "mongoose";
import { categoriaRouter } from "./routes/categorias.route.js";
import { imagenRouter } from "./routes/imagen.routes.js";

const app = express();
app.use(json());
app.use(categoriaRouter);
app.use(imagenRouter);
const PORT = process.env.PORT ?? 3000;

app.listen(PORT, async () => {
  console.log(`servidor corriendo en el puerto ${PORT}`);
  try {
    await mongoose.connect(process.env.MONGODB);
    console.log("se conecto a la base de datos");
  } catch (error) {
    console.log(error);
  }
});
