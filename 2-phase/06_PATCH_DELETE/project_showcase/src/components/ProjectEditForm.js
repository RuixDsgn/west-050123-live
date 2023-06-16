import { useState } from "react"

const ProjectEditForm = ({ editProject, onUpdateProjects }) => {
	const { name, about, phase, link, image, id } = editProject
	const [formData, setFormData] = useState({
		...editProject,
		// name: name
	})

	const handleChange = (e) => {
		setFormData((prevFormData) => {
			return { ...prevFormData, [e.target.name]: e.target.value }
		})
	}

	const handleSubmit = (e) => {
		e.preventDefault()
		const patchReqObj = {
			method: "PATCH",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify(formData),
		}
		fetch(`http://localhost:4000/projects/${id}`, patchReqObj)
			.then((res) => res.json())
			.then((updatedProject) => {
				onUpdateProjects(updatedProject)
			})
	}

	return (
		<section>
			<form className="form" autoComplete="off" onSubmit={handleSubmit}>
				<h3>Edit Project</h3>

				<label htmlFor="name">Name</label>
				<input
					type="text"
					id="name"
					name="name"
					onChange={handleChange}
					value={formData.name}
				/>

				<label htmlFor="about">About</label>
				<textarea
					id="about"
					name="about"
					onChange={handleChange}
					value={formData.about}
				/>

				<label htmlFor="phase">Phase</label>
				<select
					name="phase"
					id="phase"
					onChange={handleChange}
					value={formData.phase}
				>
					<option value={""}>Select One</option>
					<option value="1">Phase 1</option>
					<option value="2">Phase 2</option>
					<option value="3">Phase 3</option>
					<option value="4">Phase 4</option>
					<option value="5">Phase 5</option>
				</select>

				<label htmlFor="link">Project Homepage</label>
				<input
					type="text"
					id="link"
					name="link"
					onChange={handleChange}
					value={formData.link}
				/>

				<label htmlFor="image">Screenshot</label>
				<input
					type="text"
					id="image"
					name="image"
					onChange={handleChange}
					value={formData.image}
				/>

				<button type="submit">Edit Project</button>
			</form>
		</section>
	)
}

export default ProjectEditForm
