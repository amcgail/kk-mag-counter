def genlim(limit):
    def limiter(gen):
        for i,item in enumerate(gen):
            if i > limit:
                break
            yield item
    return limiter