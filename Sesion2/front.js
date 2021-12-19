const URL = "http://127.0.0.1:5000/productos"

// FETCH THEN CATCH
// fetch(URL,{method:"GET"})
// .then((response) => {
//     return response.json()
// })
// .then((data) => {
//     console.log(data)
// })
// .catch((error) => {
//     console.error(error)
// })

// fetch(URL, {
//   method: "POST",
//   body: JSON.stringify({
//     nombre: "Paneton con arto bromato",
//     precio: 17.5,
//     disponible: true,
//     fecha_vencimiento: "2022-01-14",
//   }),
//   headers: {
//     "Content-Type": "application/json",
//   },
// })
//   .then((response) => {
//     return response.json();
//   })
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((error) => {
//     console.error(error);
//   });

// FETCH ASYNC AWAIT
// const getData = async () => {
//     try {
//         const response = await fetch(URL,{method:"GET"})
//         const data = await response.json()
//         console.log(data)
//     } catch (error) {
//         throw error
//     }
// }
// getData()

// const postData = async () => {
//     try {
//         const enviar = await fetch(URL,{method:"POST",body: JSON.stringify({
//             nombre: "Paneton con arto bromato",
//             precio: 17.5,
//             disponible: true,
//             fecha_vencimiento : "2022-01-14"
//         }),headers:{
//             "Content-Type" : "application/json"
//         }})
//         const data = await enviar.json()
//         console.log(data)
//     } catch (error) {
//         throw error
//     }
// }
// postData()

// AXIOS THEN CATCH
// axios
//   .get("http://127.0.0.1:5000/productos")
//   .then((response) => {
//     console.log(response.data);
//   })
//   .catch((error) => {
//     console.error(error);
//   });

// axios
//   .post("http://127.0.0.1:5000/productos", {
//     nombre: "Paneton con arto bromato",
//     precio: 17.5,
//     disponiblre: true,
//     fecha_vencimiento: "2022-01-14",
//   })
//   .then((response) => {
//     console.log(response.data);
//   })
//   .catch((error) => {
//     console.error(error);
//   });

// AXIOS ASYNC AWAIT
const getData = async() => {
    try {
        const {data} = await axios.get(URL)
        console.log(data)
    } catch (error) {
        throw error
    }
}
getData()

const postData = async () => {
    try {
        const {data} = await axios.post(URL,{
                nombre : "Paneton con arto bromato",
                precio : 17.5,
                disponible: true,
                fecha_vencimiento : "2022-01-14"
            })
        console.log(data)
    } catch (error) {
        throw error
    }
}
postData()