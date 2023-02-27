import './Footer.css'

const Footer = () => {
  return (
    <div className='footerMainDiv'>
      <div className='footerInfo'>
        <div>
          <p>Shootstarter by Ned Nguyen, 2023</p>
        </div>
        <div className='footerLink'>
          <a href='https://github.com/nedned1108/capstone-project-shootstarter'>{<i class="fa-brands fa-github"></i>}</a>
          <a href='https://www.linkedin.com/in/ned-nguyen-693575257/'>{<i class="fa-brands fa-linkedin"></i>}</a>
        </div>
      </div>
      <div className='footerTech'>
        <p>Javascript</p>
        <p>React</p>
        <p>Redux</p>
        <p>HTML</p>
        <p>CSS</p>
        <p>Python</p>
        <p>Flask Server</p>
      </div>
      <img src='https://ksr-static.imgix.net/c51lnrg9-doodle_continue.png?ixlib=rb-2.1.0&auto=compress%2Cformat&w=1000&fit=min&s=dc34091fa7d24f5d676e0e0201337f9b'/>
    </div>
  )
}

export default Footer;