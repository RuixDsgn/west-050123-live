import { useNavigate } from "react-router"
// use Nav is the same as useHistory
const Production = ({ production, setEditProduction, deleteProduction }) => {
	const { title, director, image, id } = production
	const nav = useNavigate()

	const handleEditButton = (e) => {
		setEditProduction(production)
		nav(`/productions/edit/${production.id}`)
	}

	const handleDeleteButton = (e) => {
		console.log(id)
		deleteProduction(id)
	}

	return (
		<div>
			<hr />
			<h2>{title}</h2>
			<h2>{director}</h2>
			<img src={image} alt={title} onClick={() => nav(`/productions/${id}`)} />
			<button onClick={handleEditButton}>EDIT</button>
			<button onClick={handleDeleteButton}>DELETE</button>
			<hr />
		</div>
	)
}

export default Production
