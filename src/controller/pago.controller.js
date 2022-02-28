import { PagoService } from "../services/pagos.service.js";

export async function crearPreferencia(req, res) {
  const resultado = await PagoService.generarPreferenciaDePago(req.body);
  return res.status(201).json(resultado);
}

export function recibirNotificacion(req, res) {
  console.log("los query params son: ");
  console.log(req.params);
  PagoService.recibirNotificacion(req.body);
  return res.status(200).send();
}
