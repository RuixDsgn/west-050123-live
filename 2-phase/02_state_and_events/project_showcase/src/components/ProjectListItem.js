import { useState } from "react"

const ProjectListItem = (props) => {

const [clapCount, setClapCount] = useState(0)

const handleClaps = (e) => {
	setClapCount((clapCount) => (clapCount + 1))
}

	return (
		<li className="card">
			<figure className="image">
				<img src={props.project.image} alt={props.project.name} />
				<button onClick={handleClaps} className="claps">
					👏{clapCount}
				</button>
			</figure>

			<section className="details">
				<h4>{props.project.name}</h4>
				<p>{props.project.about}</p>
				{props.project.link ? (
					<p>
						<a href={props.project.link}>Link</a>
					</p>
				) : null}
			</section>

			<footer className="extra">
				<span className="badge blue">Phase {props.project.phase}</span>
			</footer>
		</li>
	)
}

export default ProjectListItem


/* Incrementing the Claps Button Amount
	- Set state variable and setter function (i.e. line 5)
	- Create a function that will use the setter function to increment the state variable (i.e line 7)
	- Add an onClick event on the target button (i.e. line 15) and call on the function targeting the setter function
*/