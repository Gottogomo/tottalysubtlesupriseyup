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

LOGGER = get_logger(__name__)


def run():
    
    st.markdown("<h1 style='font-size:58px'>🌸Happy Mother's Day!👋<h1/>",unsafe_allow_html=True)
    st.write("---")

    st.write("""I'm sorry we couldn't spend another 
             Mother's Day together. It didn't help I forgot stuff to make a card, so I thought
             I would try to make that up by doing this!""")
    
    st.markdown('<a style="text-decoration: none;" href="https://docs.google.com/document/d/1od_IhgoLG5NO5-s3aOH4C6pUZok5M1-E5ReltRNxmLM/edit?usp=sharing">Docs</a>',unsafe_allow_html=True)
    st.markdown("<img src='https://drive.google.com/file/d/1Eg7KFkqPlijYMoI94C6IYdT-huWc1jQ7/view?usp=drive_link'/>", unsafe_allow_html=True)
    


if __name__ == "__main__":
    run()
