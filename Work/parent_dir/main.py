import fileparse
import logging
log = logging.getLogger(__name__)

if __name__ == '__main__':

	logging.basicConfig(level = logging.DEBUG)
	#logging.getLogger('fileparse').level = logging.
	log.warning('warning outside fileparse')
	log.debug('debug outside fileparse')
	#logging.basicConfig(level = logging.DEBUG)
	#logging.basicConfig(filename = 'app.log', filemode = 'w', level = logging.DEBUG )
	opts = {'silence_errors': True, 'has_headers': True}
	fileparse.read_portfolio('Data/missing.csv', columns_select = ['name', 'shares', 'price'], types = [str,int,float],**opts)