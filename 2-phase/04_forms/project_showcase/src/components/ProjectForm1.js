import { useState } from "react"

/* 
  ? VANILLA JS
  1. Find the form and addEventLister
    - document.getElementById("form").addEventListener("submit", handleSubmit)
  2. (Inside The handler) e.preventDefault()
  3. Build an Obj by finding the input values on the form
  3.5. Optional - persist with a POST Request
  4. With that obj, we append/prepend/put on the page in some way

  
  * React Forms
  1. On the <form> element, onSubmit={handleSubmit}
  2. (Inside The handler) e.preventDefault()
  3. Inputs need to be defined in STATE!
    3.1 - Set each input to it's own indenpendent state
    3.2 - Set the WHOLE FORM to a full object of keys(inputs) and values
    3.3 - Attach `ref` to each input, i.e. a tracker on each input and get the current value at the time of submitting
  4. Update our `project` state in the ProjectContainer component to add this new obj
    - This will trigger a re-render, and will have ALL the functionality of each project
    


  Tangent - Spread Operator
  
  
  ! ARRAY METHODS IN REACT STATE
  .push(append) => setState([...prevState, newObj])
  .unshift(prepend) => setState([newObj, ...prevState])
  .remove => setState(prevState.filter(x => x.id !== someid))
  .update => setState(prevState.map(x => when x is the element to update, update, else just pass through the old data))


*/

const ProjectForm1 = ({ setProjects }) => {
	const [formData, setFormData] = useState({
		name: "",
		about: "",
		phase: "",
		link: "",
		image: "",
	})

	const handleNameChange = (e) => {
		// setFormData({ name: e.target.value, about: formData.about, phase: formData.phase, link: formData.link })
		setFormData({ ...formData, name: e.target.value })
	}

	const handleChangeAll = (e) => {
		setFormData((prevFormData) => {
			return { ...prevFormData, [e.target.name]: e.target.value }
		})
	}

	const handleSubmit = (e) => {
		e.preventDefault()
		console.log(formData)
		// setProjects([newProjObj, ...projects])
		setProjects((prevState) => [formData, ...prevState])
	}

	return (
		<section>
			<form className="form" autoComplete="off" onSubmit={handleSubmit}>
				<h3>Add New Project</h3>

				<label htmlFor="name">Name</label>
				<input type="text" id="name" name="name" onChange={handleNameChange} />

				<label htmlFor="about">About</label>
				<textarea
					id="about"
					name="about"
					onChange={(e) => setFormData({ ...formData, about: e.target.value })}
				/>

				<label htmlFor="phase">Phase</label>
				<select name="phase" id="phase" onChange={handleChangeAll}>
					<option value={""}>Select One</option>
					<option value="1">Phase 1</option>
					<option value="2">Phase 2</option>
					<option value="3">Phase 3</option>
					<option value="4">Phase 4</option>
					<option value="5">Phase 5</option>
				</select>

				<label htmlFor="link">Project Homepage</label>
				<input type="text" id="link" name="link" onChange={handleChangeAll} />

				<label htmlFor="image">Screenshot</label>
				<input type="text" id="image" name="image" onChange={handleChangeAll} />

				<button type="submit">Add Project</button>
			</form>
		</section>
	)
}

export default ProjectForm1
