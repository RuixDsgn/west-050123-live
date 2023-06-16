import ProjectListItem from "./ProjectListItem"

const ProjectList = ({ projects }) => {
	const projectListItems = projects.map((project) => (
		<ProjectListItem key={project.id} {...project} />
	))

	return <ul className="cards">{projectListItems}</ul>
}

export default ProjectList
