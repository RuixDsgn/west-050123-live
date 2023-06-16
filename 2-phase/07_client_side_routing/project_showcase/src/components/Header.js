import { NavLink } from "react-router-dom"

const Header = ({ isDarkMode, setIsDarkMode }) => {
	const handleClick = () => setIsDarkMode(!isDarkMode)

	const buttonTextContent = isDarkMode ? "Dark Mode" : "Light Mode"

	return (
		<header>
			<h1>
				<span className="logo">
					<NavLink to="/">
						<button>{"//"}</button>
					</NavLink>
				</span>
				Project Showcase
			</h1>
			<div className="navigation">
				{/* <a href="/projects" >All Projects</a> */}
				<NavLink to="/projects">
					<button>All Projects</button>
				</NavLink>
				<NavLink to="/projects/new">
					<button>Add Project</button>
				</NavLink>
			</div>
			<button onClick={handleClick}>{buttonTextContent}</button>
		</header>
	)
}

export default Header
