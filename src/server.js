import express, { json } from "express";
import mongoose from "mongoose";
import { productoRouter } from "./routes/producto.routes.js";
import { categoriaRouter } from "./routes/categoria.route.js";
import { categoriaProductoRouter } from "./routes/categoria_producto.routes.js";
import mercadopago from "mercadopago";
import { pagoRouter } from "./routes/pago.routes.js";
import { clienteRouter } from "./routes/cliente.routes.js";

mercadopago.configure({
  access_token: process.env.ACCESS_TOKEN_MP,
  integrator_id: process.env.INTEGRATOR_ID_MP,
});

const app = express();
const PORT = process.env.PORT ?? 3000;

app.use(json());

app.use(productoRouter);
app.use(categoriaRouter);
app.use(categoriaProductoRouter);
app.use(pagoRouter);
app.use(clienteRouter);

app.listen(PORT, async () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
  try {
    await mongoose.connect(
      process.env.NODE_ENV === "production"
        ? process.env.DATABASE_URL
        : process.env.DATABASE_URL_DEV
    );
    console.log("Bd sincronizada exitosamente");
  } catch (error) {
    console.log("Error al conectarse con la bd ❌");
  }
});
