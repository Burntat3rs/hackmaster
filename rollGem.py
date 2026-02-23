def roll_gems(rolls):
    for i in range(rolls):
        random_gem_table = get_table_category(gemstones_category)
        index_list = split_index_from_table(random_gem_table, 2)
        
        random_gem = random.choices(
        population=random_gem_table,
        weights=index_list,
        )
        random_gem = random_gem[0]
        random_size = random.choices(
        population=gem_size,
        weights=split_index_from_table(gem_size, 1),
        )

        random_quality = get_gem_quality()

        gem = Gem(random_gem[0], random_gem[1], random_gem[2], random_size[0], random_quality, "gem")
        return gem    
