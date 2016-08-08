for obj in population:
    country = obj['country']
    population = obj['population']
    b = CountryModel(country=country,population=population)
    b.save()

for obj in life_expectancy:
    try:
	    b = CountryModel.objects.get(country=obj['country'])
		b.life_expectancy = obj['expectancy']
		b.save()
	except Exception as e:
		continue

for obj in surface_area:
        try:
            b = CountryModel.objects.get(country=obj['country'])
            b.area = obj['area']
            b.save()
        except:
            continue

for obj in population_density:
        try:
            b = CountryModel.objects.get(country=obj['country'])
            b.density = obj['density']
            b.save()
        except Exception as e:
            continue

for obj in elevation:
        try:
            b = CountryModel.objects.get(country=obj['country'])
            den = obj['average'][:-1]
            b.elevation = den
            b.save()
        except Exception as e:
            continue
