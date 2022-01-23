import {Prisma} from "../prisma.js"

export const crearCategoria = async (req,res) => {
    const data = req.body
    const content = await Prisma.categoria.create({data})
    return res.status(201).json({content})
}

export const listarCategoria = async (req,res) => {
    const categorias = await Prisma.categoria.findMany({})
    return res.json({ 
        content: categorias 
    })
}

export const buscarCategoria = async (req,res) => {
    const params = req.query
    if(params.estado){
        params.estado = params.estado === "true" ? true : false
    }
    const categorias = await Prisma.categoria.findMany({where: params})
        return res.json({
            content: categorias
        })
}

export const actualizarCategoria = async (req,res) => {
    const id = +req.params.id
    try {
        await Prisma.categoria.findUnique({where: {id:id}})
        const categoriaActualizada = await Prisma.categoria.update({data: req.body, where: {id}})
        return res.status(201).json({
            content: categoriaActualizada
        })
    } catch (error) {
        return res.status(400).json({
            message: "Error al actualizar la categoria"
        })
    }
}