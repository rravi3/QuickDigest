import React from 'react'

const MainView = () => {
    return (
        <div class="landing-page-wrapper">
            <div class="landing-page-content">
                <div class="title">
                    <h1>
                        Note Nugget
                    </h1>

                </div>
                <div class="subheading">
                    <span>
                        Paste text:
                    </span>
                </div>
                <div class="user-input-wrapper">
                    <div class="user-input-content">
                        <textarea class="input-area" id="input-area" rows="4" cols="50"></textarea>
                    </div>
                </div>
                <div class="generate-output-button-wrapper">
                    <button class="generate-output-button">
                        Generate
                    </button>
                </div>
                <div class="output-nuggets-wrapper">

                </div>
            </div>


        </div>
    )
}

export default MainView