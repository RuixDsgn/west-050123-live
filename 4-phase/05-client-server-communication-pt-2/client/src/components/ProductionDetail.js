import { useEffect, useState } from "react"
import CastMemberDetail from "./CastMemberDetail"
import { useParams } from "react-router-dom"

const ProductionDetail = () => {
	const [productionDetail, setProductionDetail] = useState({})
	const { title, director, description, image, ongoing, cast_members, genre } =
		productionDetail
	const { id } = useParams()
	useEffect(() => {
		fetch(`http://127.0.0.1:5555/productions/${id}`)
			.then((res) => res.json())
			.then((oneProd) => {
				console.log(oneProd)
				setProductionDetail(oneProd)
			})
	}, [id])

	const mappedCastMembers = () => {
		return cast_members.map((castMember) => (
			<CastMemberDetail {...castMember} key={castMember.id} />
		))
	}

	return (
		<div>
			<h1>
				{title} : {director}
			</h1>
			Can you see it: {ongoing ? "Yup!" : "Nah.."}
			<h1>{genre} </h1>
			<img src={image} alt={title} />
			<p>{description} </p>
			<ul>{cast_members ? mappedCastMembers() : null}</ul>
		</div>
	)
}

export default ProductionDetail
