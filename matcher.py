def find_best_match(buyers, sellers):

    matches = []

    for buyer in buyers:

        best_seller = None
        best_score = -1

        for seller in sellers:

            if buyer.payment != seller.payment:
                continue

            price_diff = abs(buyer.price - seller.price)

            score = seller.trust_score * 2 - price_diff

            if score > best_score:

                best_score = score
                best_seller = seller

        if best_seller:

            matches.append({
                "buyer": buyer.id,
                "seller": best_seller.id,
                "score": best_score
            })

    return matches