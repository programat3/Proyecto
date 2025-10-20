from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pydantic_ai import RunContext, Tool


def test_python_org_search(ctx: RunContext[str]) -> str:
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(ctx.deps)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.implicitly_wait(2)
    elem2 = driver.find_element(By.PARTIAL_LINK_TEXT, ctx.deps)
    elem2.click()
    curr_link = driver.current_url
    driver.close()
    return curr_link
