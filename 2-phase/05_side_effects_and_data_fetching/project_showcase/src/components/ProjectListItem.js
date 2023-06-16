import { useEffect, useState } from "react"

const ProjectListItem = ({ id, about, image, link, name, phase }) => {
	const [clapCount, setClapCount] = useState(0)

	useEffect(() => {
		console.log(`mounted of name: ${name}`)

		return () => {
			console.log("Unmounting List Item: ", name)
		}
	}, [])

	// useEffect(() => {
	// 	console.log("Been Clapped: ", clapCount)
	// }, [link])

	const handleClap = () => setClapCount(clapCount + 1)

	return (
		<li className="card">
			<figure className="image">
				<img src={image} alt={name} />
				<button className="claps" onClick={handleClap}>
					👏{clapCount}
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
			</footer>
		</li>
	)
}

export default ProjectListItem
