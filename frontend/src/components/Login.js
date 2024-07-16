import React, { useState } from 'react'
import './Login.css'

const Login = () => {
    
    return (
        <div className='login-container'>
            <form className='login-form'>
                <div className='form-group'>
                    <label htmlFor='username'>Username</label>
                    <input type='text' id='username' name='username' placeholder='Enter your username: ' />
                </div>
                <div className='form-group'>
                    <label htmlFor='email'>Email</label>
                    <input type='email' id='email' name='email' placeholder='Enter your email: ' />
                </div>
                <div className='form-group'>
                    <label htmlFor='password'>Password</label>
                    <input type='password' id='password' name='password' placeholder='Enter your password: ' />
                </div>
                <button type='submit' className='submit-button'>Submit</button>
            </form>
        </div>
    )
}

export default Login
