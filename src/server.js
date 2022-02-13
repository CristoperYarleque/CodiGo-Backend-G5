import express, { json } from "express";
import mongoose from "mongoose";
import { categoriaRouter } from "./routes/categorias.route.js";
import { imagenRouter } from "./routes/imagen.routes.js";
import { fileURLToPath } from "url";
import { dirname } from "path";
import { usuarioRouter } from "./routes/usuario.routes.js";
import sgMail from "@sendgrid/mail";

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const direccion_proyecto = dirname(fileURLToPath(import.meta.url));

const app = express();
app.use(json());
app.use(categoriaRouter);
app.use(imagenRouter);
app.use(usuarioRouter);

app.use("/src/media", express.static(direccion_proyecto + "/media"));

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
