import { NavLink } from "react-router-dom"

const Nav = () => {
  return (
    <div>
      <NavLink to="/">Home</NavLink>
      <NavLink to="/productions">Productions</NavLink>
      <NavLink to="/productions/new">Add a Production</NavLink>
    </div>
  )
}

export default Nav