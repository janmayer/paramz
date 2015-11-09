#===============================================================================
# Copyright (c) 2012 - 2014, GPy authors (see AUTHORS.txt).
# Copyright (c) 2015, Max Zwiessele
#
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of paramax nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#===============================================================================

from .model import Model
from .parameterized import Parameterized
from .param import Param
from .core.observable_array import ObsAr
from paramz import transformations as constraints
from . import caching

def load(file_or_path):
    """
    Load a previously pickled model, using `m.pickle('path/to/file.pickle)'`

    :param file_name: path/to/file.pickle
    """
    try:
        import cPickle as pickle
        if isinstance(file_or_path, basestring): 
            with open(file_or_path, 'rb') as f:
                m = pickle.load(f)
        else:
            m = pickle.load(file_or_path)
    except: #python3
        import pickle
        if isinstance(file_or_path, str): 
            with open(file_or_path, 'rb') as f:
                m = pickle.load(f)
        else:
            m = pickle.load(file_or_path)
    return m