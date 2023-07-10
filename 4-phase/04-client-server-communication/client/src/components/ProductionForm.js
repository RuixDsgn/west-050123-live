import { useState } from "react"

const ProductionForm = ({postProduction}) => {
	const [formData, setFormData] = useState({
		title: "",
		genre: "",
		budget: 0,
		director: "",
		description: "",
    image: ""
	})

	const handleSubmit = (e) => {
		e.preventDefault()
		console.log(formData)
    postProduction(formData)
	}

	const handleChange = (e) => {
		setFormData({
			...formData,
			[e.target.name]: e.target.value,
		})
	}

	return (
		<div>
			<h1>Add a New Production!</h1>
			<form onSubmit={handleSubmit}>
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
					<input
						name="image"
						value={formData.image}
						onChange={handleChange}
					/>
				</label>
        <br />
        <input type="submit" value="ADD YOUR NEW PRODUCTION" />
			</form>
		</div>
	)
}

export default ProductionForm
