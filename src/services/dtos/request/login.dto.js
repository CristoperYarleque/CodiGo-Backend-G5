import validator from "validator";

export function loginDto({ correo, password }) {
  if (!validator.isEmail(correo)) {
    throw Error("El correo debe ser un correo valido");
  }
  if (!validator.isStrongPassword(password)) {
    throw Error("La contrasña no es segura");
  }

  return { correo, password };
}
