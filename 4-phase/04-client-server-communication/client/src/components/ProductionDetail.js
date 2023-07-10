import { useEffect, useState } from "react"
import { useParams } from "react-router"

const ProductionDetail = () => {
	const [productionDetail, setProductionDetail] = useState({})
	const { id } = useParams()
	useEffect(() => {
		fetch(`http://127.0.0.1:5555/productions/${id}`)
			.then((res) => res.json())
			.then((oneProd) => {
				console.log(oneProd)
				setProductionDetail(oneProd)
			})
	})
	return (
		<div>
			<h1>{productionDetail.title} </h1>
			<h1>{productionDetail.genre} </h1>
			<img src={productionDetail.image} alt={productionDetail.title} />
			<p>{productionDetail.description} </p>
		</div>
	)
}

export default ProductionDetail
