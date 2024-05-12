# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import requests

LOGGER = get_logger(__name__)


def run():
    
    st.markdown("<h1 style='font-size:58px'>🌸Happy Mother's Day!👋<h1/>",unsafe_allow_html=True)
    st.write("---")

    st.write("""I'm sorry we couldn't spend another 
             Mother's Day together. It didn't help I forgot stuff to make a card, so I thought
             I would try to make that up by doing this!""")
    
    st.markdown ("<img src='https://mir-s3-cdn-cf.behance.net/project_modules/hd/52cb1440701143.57894f325a820.gif' style='border: 5px solid #050505;width: 100%;height: auto;border-radius:80%' />", unsafe_allow_html=True)

    st.write("---")
    st.write("For one, your favorite child won't stop talking about you")
    with st.expander("🐕‍🦺",False):
        # iamge ID
        file_id = "1-3DDyh4AAC-v6mmaPOXS3l-oAnUuMS2c"
        # URL
        url = f"https://drive.google.com/uc?export=view&id={file_id}"
        response = requests.get(url)
        st.image(response.content)

    st.write("---")
    st.write("I also heard a lot may be changing.")

    with st.expander("🎉",False):
            st.write("New Career Oppurtunites")
            st.markdown("<img src='data:image/jpeg;base64,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' />",unsafe_allow_html=True)
    
    with st.expander("🎉",False):
            st.write("Education!")
            st.markdown("<img src='data:image/jpeg;base64,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' />",unsafe_allow_html=True)
      
    with st.expander("🎉",False):
            st.write("And time to do more...?")
            st.markdown("<img src='https://render.fineartamerica.com/images/images-new-artwork/images/artworkimages/medium/3/woman-floral-head-vintage-pencil-drawing-mounir-khalfouf.jpg' />",unsafe_allow_html=True)

           


    st.write("---")

    st.write(" ")
    st.write("I think for all that, you deserve some gifts.")

    # with st.expander("🎉",False):
    #         st.write(" ")
    #         st.write("One Free Purchase")

    with st.expander("🎊",False):
            st.write(" ")
            st.write("$50 for Amazon (whenever I can figure that out)")
            st.markdown("<img style='width: 100%;height: auto;' src='https://m.media-amazon.com/images/I/51MRE8TVg6L._QL92_SH45_.jpg' />",unsafe_allow_html=True)
            
    with st.expander("💝",False):
            st.write(" ")
            st.write("One big big hug whenever I am around (free of charge)")
            st.markdown("<img style='width: 100%;height: auto;' src='https://www.icegif.com/wp-content/uploads/2023/07/icegif-334.gif' />",unsafe_allow_html=True)

    with st.expander("🎁",False):
            file_id1 = "1Eg7KFkqPlijYMoI94C6IYdT-huWc1jQ7"
            # URL
            urlyup1 = f"https://drive.google.com/uc?export=view&id={file_id1}"
            response = requests.get(urlyup1)
            st.write("Front and Back:")
            st.write(urlyup1)

            file_id2 = "1eBs_SiDLrpod50X0_tq95TA5mgZ9IUnp"
            # URL
            urlyup2 = f"https://drive.google.com/uc?export=view&id={file_id2}"
            response = requests.get(urlyup2)
            st.write("Inside:")
            st.write(urlyup2)


    



    

  

if __name__ == "__main__":
    run()
