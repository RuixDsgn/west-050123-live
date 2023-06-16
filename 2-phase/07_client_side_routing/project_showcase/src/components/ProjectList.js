import ProjectListItem from "./ProjectListItem"

const ProjectList = ({ projects, onUpdateProjects, onDeleteProject }) => {
	const projectListItems = projects.map((project) => (
		<ProjectListItem
			key={project.id}
			{...project}
			onUpdateProjects={onUpdateProjects}
			onDeleteProject={onDeleteProject}
		/>
	))

	return <ul className="cards">{projectListItems}</ul>
}

export default ProjectList
