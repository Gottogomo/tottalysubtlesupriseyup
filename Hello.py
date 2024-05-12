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
    
    st.markdown ("<img src='https://mir-s3-cdn-cf.behance.net/project_modules/hd/52cb1440701143.57894f325a820.gif' style='border: 5px solid #050505;width: 100%;height: auto;' />", unsafe_allow_html=True)

    

    


    # iamge ID
    file_id = "1-3DDyh4AAC-v6mmaPOXS3l-oAnUuMS2c"
    # URL
    url = f"https://drive.google.com/uc?export=view&id={file_id}"
    response = requests.get(url)
    st.image(response.content)

    

  

if __name__ == "__main__":
    run()
