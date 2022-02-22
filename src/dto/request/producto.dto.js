import validator from "validator";

export function productoDto({ nombre, precio, tipo, estado }) {
  if (validator.isEmpty(nombre)) {
    throw Error("el nomnre no puede estar vacio");
  }
  if (!validator.isInt(precio.toString()) && +precio < 0) {
    throw Error("el precio no puede ser negativo");
  }
  if (tipo !== "ABARROTES" && tipo !== "HIGIENE PERSONAL" && tipo !== "OTROS") {
    throw Error("el tipo debe ser 'ABARROTES','HIGIENE PERSONAL','OTROS'");
  }
  if (estado && !validator.isBoolean(estado)) {
    throw Error("el estado tiene que ser true o false");
  }

  return { nombre, precio, tipo, estado };
}
