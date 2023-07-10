import { useState } from "react"
// import { useParams } from "react-router-dom"

const ProductionEditForm = ({ patchProduction, editProduction }) => {
	const [formData, setFormData] = useState({ ...editProduction })

	const handleEditSubmit = (e) => {
		e.preventDefault()
		console.log(formData)
		patchProduction(
			{
				title: formData.title,
				genre: formData.genre,
				budget: formData.budget,
				image: formData.image,
				description: formData.description,
				director: formData.director,
			},
			editProduction.id
		)
	}

	const handleChange = (e) => {
		setFormData({
			...formData,
			[e.target.name]: e.target.value,
		})
	}

	return (
		<div>
			<h1>Edit a Your Production!</h1>
			<form onSubmit={handleEditSubmit}>
				<label>
					TITLE:
					<input name="title" value={formData.title} onChange={handleChange} />
				</label>
				<br />
				<label>
					GENRE:
					<input name="genre" value={formData.genre} onChange={handleChange} />
				</label>
				<br />
				<label>
					BUDGET:
					<input
						name="budget"
						type="number"
						value={formData.budget}
						onChange={handleChange}
					/>
				</label>
				<br />
				<label>
					DIRECTOR:
					<input
						name="director"
						value={formData.director}
						onChange={handleChange}
					/>
				</label>
				<br />
				<label>
					DESCRIPTION:
					<input
						name="description"
						value={formData.description}
						onChange={handleChange}
					/>
				</label>
				<br />
				<label>
					IMAGE:
					<input name="image" value={formData.image} onChange={handleChange} />
				</label>
				<br />
				<input type="submit" value="UPDATE YOUR NEW PRODUCTION" />
			</form>
		</div>
	)
}

export default ProductionEditForm
