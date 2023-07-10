import React from "react"

const CastMemberDetail = ({ id, name, role }) => {
	return (
		<li>
			{role} played by: {name}{" "}
		</li>
	)
}

export default CastMemberDetail
