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

    st.write("---")
    st.write(" ")
    st.write("I think for all that, you deserve some gifts.")

    # with st.expander("🎉",False):
    #         st.write(" ")
    #         st.write("One Free Purchase")
            
    with st.expander("💝",False):
            st.write(" ")
            st.write("One big big hug whenever I am around (free of charge)")
            st.markdown("<img src='https://www.icegif.com/wp-content/uploads/2023/07/icegif-334.gif' />",unsafe_allow_html=True)

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


    


    # iamge ID
    file_id = "1-3DDyh4AAC-v6mmaPOXS3l-oAnUuMS2c"
    # URL
    url = f"https://drive.google.com/uc?export=view&id={file_id}"
    response = requests.get(url)
    st.image(response.content)

    

  

if __name__ == "__main__":
    run()
