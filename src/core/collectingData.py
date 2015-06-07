#*- coding: utf-8 -*- 
#
#            Copyright (C) 2015 QDevor
#
#  Licensed under the GNU General Public License, Version 3.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#            http://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

from sqlalchemy import create_engine
from pandas.io.pytables import HDFStore
import tushare as ts
from tushare.util import dateu as du

import coreMisc as cmisc
# import from parent directory
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import misc as _misc

def xls(code='000878'):
    df = ts.get_hist_data(code)
    #直接保存
    save_dir = _misc.getDir('data')
    df.to_excel(save_dir + '/' + code + '.xlsx')
    #df.to_excel(save_dir + code + '.xlsx', startrow=2,startcol=5)

def db(code='000878'):
	#print (code, du.last_tddate())
	df = ts.get_tick_data(code,date=du.last_tddate()) # 获取分笔数据 up to last trade day
	#df = ts.get_today_ticks(code) # 获取当日分笔明细数据
	engine = create_engine('mysql://root:123456@127.0.0.1/mystock?charset=utf8')
#		db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db="mystock",charset="utf8")
#		df.to_sql('TICK_DATA',con=db,flavor='mysql')
#		db.close()
	df.to_sql('tick_data',engine,if_exists='append')