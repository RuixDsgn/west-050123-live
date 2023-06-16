import { useEffect, useState } from "react"

const ProjectListItem = ({
	id,
	about,
	image,
	link,
	name,
	phase,
	claps,
	onUpdateProjects,
	onDeleteProject,
}) => {
	// const [clapCount, setClapCount] = useState(claps ? claps : 0)

	useEffect(() => {
		console.log(`mounted of name: ${name}`)

		return () => {
			console.log("Unmounting List Item: ", name)
		}
	}, [])

	// const handleClap = () => setClapCount(clapCount + 1)

	const patchClap = () => {
		const patchReqObj = {
			method: "PATCH",
			headers: {
				"content-type": "application/json",
			},
			body: JSON.stringify({ claps: claps ? claps + 1 : 1 }),
		}
		fetch(`http://localhost:4000/projects/${id}`, patchReqObj)
			.then((res) => res.json())
			.then((updatedProject) => {
				console.log(updatedProject)
				// setClapCount(clapCount + 1)
				// setClapCount(updatedProject.claps)
				onUpdateProjects(updatedProject)
			})
	}

	const handleDelete = (e) => {
		console.log(id)
		fetch(`http://localhost:4000/projects/${id}`, {
			method: "DELETE",
		}).then(() => {
			onDeleteProject(id)
		})
	}

	return (
		<li className="card">
			<figure className="image">
				<img src={image} alt={name} />
				<button className="claps" onClick={patchClap}>
					👏{claps ? claps : 0}
				</button>
			</figure>

			<section className="details">
				<h4>{name}</h4>
				<p>{about}</p>
				{link ? (
					<p>
						<a href={link}>Link</a>
					</p>
				) : null}
			</section>

			<footer className="extra">
				<span className="badge blue">Phase {phase}</span>
				<span className="badge">
					<button onClick={handleDelete}>DELETE</button>
				</span>
			</footer>
		</li>
	)
}

export default ProjectListItem
