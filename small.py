from flask import Flask, redirect, request
import logging

logging.basicConfig(filename='record.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask('basic app')

@app.route('/')
def main():
  app.logger.debug("Debug log level")
  app.logger.info("Program running correctly")
  app.logger.warning("Warning; low disk space!")
  app.logger.error("Error!")
  app.logger.critical("Program halt!")
  return "<h1>Uodfiod Logger levels!</h1>"

if __name__ == '__main__':
  app.run(debug=True, port=5001)