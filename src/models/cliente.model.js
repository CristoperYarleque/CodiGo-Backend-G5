import mongoose from "mongoose";

const direccionSchema = new mongoose.Schema(
  {
    zip: { type: mongoose.Schema.Types.String, minlength: 2 },
    calle: mongoose.Schema.Types.String,
    numero: mongoose.Schema.Types.Number,
  },
  { _id: false }
);

const clienteSchema = new mongoose.Schema({
  nombre: mongoose.Schema.Types.String,
  apellido: mongoose.Schema.Types.String,
  correo: { type: mongoose.Schema.Types.String, unique: true },
  direccion: direccionSchema,
});

export const Cliente = mongoose.model("clientes", clienteSchema);
