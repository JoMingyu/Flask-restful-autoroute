from setuptools import setup

setup(name='flask- restful-autoroute',
      version='0.1',
      url='https://github.com/JoMingyu/Flask-restful-autoroute',
      license='MIT',
      author='PlanB',
      author_email='city7310@naver.com',
      description='Blueprint based auto routing library for flask-restful',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=['flask_restful_autoroute'],
      install_requires=['reflections', 'flask', 'flask-restful', 'flask-restful-swagger-2'])
