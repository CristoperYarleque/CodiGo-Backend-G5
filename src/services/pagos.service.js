import { preferences } from "mercadopago";

export class PagoService {
  static async generarPreferenciaDePago() {
    try {
      await preferences.create({
        payer: {
          name: "Cristoper",
          surname: "Yarleque",
          address: {
            zip_code: "20000",
            street_name: "avenida chulucanas",
            street_number: "141",
          },
          email: "caypsaturno@gmail.com",
          identification: {
            type: "DNI",
            number: "48874584",
          },
        },
        items: [
          {
            id: "1234",
            title: "zapatillas de runing",
            quantity: 1,
            unit_price: 115.0,
            currency_id: "PEN",
          },
        ],
        auto_return: "approved",
      });
    } catch (error) {
      console.log(error);
    }
  }
}
