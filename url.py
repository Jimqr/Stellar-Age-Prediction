base_url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+'

select = [
		'pl_name',
		'st_teff',
		'st_mass',
		'st_lum',
		'st_rad',
		'st_met',
		'st_logg',
		'st_rotp',
		'st_age'
]

selected = ','.join(select)

url = f'{base_url}{selected}+from+ps&format=csv'