import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import OpenModalButton from '../OpenModalButton';
import CreateProjectModal from '../CreateProjectModal';
import './Navigation.css';
import logo from '../../images/shootstarter.png'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className='navBar'>
      <div>
        <OpenModalButton 
          buttonText="Start a project"
          modalComponent={<CreateProjectModal />}
        />
      </div>
			<div>
				<NavLink exact to="/">
          <img className='logo' src={logo} />
        </NavLink>
			</div>
			{isLoaded && (sessionUser ?
				<div>
					<ProfileButton user={sessionUser} />
				</div>
        : 
        <NavLink to="/login">
          login
        </NavLink>
			)}
		</div>
	);
}

export default Navigation;
