import validator from "validator";

export function categoriaDto({ nombre, color }) {
  if (validator.isEmpty(nombre)) {
    throw Error("el nombre no puede estar vacio");
  }
  if (!validator.isEmpty(color)) {
    throw Error("el color no puede estar vacio");
  }
  return { nombre, color };
}
