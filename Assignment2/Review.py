class Review:
    def constructor():
        pass
'''The attributes of review are id(int, default value -1), content(str, default value “”),
rating(float, default value -1.0), course_id(int, default value -1).'''

    def find_review_by_id(review_id):
        pass
'''This method has a positional argument review id(int or srt). It finds the review
information based on the given id from the review.txt file. A review object will be
returned. If not found, return None.'''
    def find_review_by_keywords(keyword):
        pass
'''This method has a positional argument keyword(str). It finds the reviews whose
content contains the given keyword from the review.txt file. A list of review objects
will be generated and returned. The result list looks like [Review(), Review(),
Review()….]. If not found, return an empty list. The keyword cannot be empty.'''
    def find_review_by_course_id(course_id):
        pass
'''This method has a positional argument course id(int or str). It finds the reviews that
belong to the given course id. A list of review objects will be generated and returned.
The result list looks like [Review(), Review(), Review()….]. If not found, return an
empty list.'''
    def reviews_overview():
        pass
'''This method returns a string that shows the total number of reviews.'''
    def __str__():
        pass
'''Return a string containing all review attributes.'''
