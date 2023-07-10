import { useNavigate } from "react-router"
// use Nav is the same as useHistory
const Production = ({ title, genre, director, description, image, id }) => {
	const nav = useNavigate()

	return (
		<div>
			<hr />
			<h2>{title}</h2>
			<h2>{director}</h2>
			<img src={image} alt={title} onClick={() => nav(`/productions/${id}`)} />
			<hr />
		</div>
	)
}

export default Production
