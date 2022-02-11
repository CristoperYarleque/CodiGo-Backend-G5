import mongoose from "mongoose";

const categoriaSchema = new mongoose.Schema({
  categoriaNombre: {
    type: mongoose.Schema.Types.String,
    alias: "nombre",
    required: true,
  },
  categoriaEstado,
  categoriaImagen,
});
