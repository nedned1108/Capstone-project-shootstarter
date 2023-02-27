import './Footer.css'

const Footer = () => {
  return (
    <div className='footerMainDiv'>
      <div>
        <p>Shootstarter by Ned Nguyen, 2023</p>
      </div>
      <div className='footerLink'>
        <a href='https://github.com/nedned1108/capstone-project-shootstarter'>{<i class="fa-brands fa-github"></i>}</a>
        <a href='https://www.linkedin.com/in/ned-nguyen-693575257/'>{<i class="fa-brands fa-linkedin"></i>}</a>
      </div>
    </div>
  )
}

export default Footer;
