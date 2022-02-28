import { PagoService } from "../services/pagos.service.js";

export async function crearPreferencia(req, res) {
  const resultado = await PagoService.generarPreferenciaDePago(req.body);
  return res.status(201).json(resultado);
}
