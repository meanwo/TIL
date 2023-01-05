import Controller from "./Controller.js";
import Store from "./store.js";
import storage from "./storage.js";
import SearchFormView from "./views/SearchFormView.js";
import SearchResultView from "./views/SearchResultView.js";
import TabView from "./views/TabView.js";
import KeywordListView from "./views/KeywordListView.js";
import HistoryListView from "./views/HistoryListView.js";

const tag = "[main]";


// DOM 콘텐츠가 로딩되었을 때 아래의 메인함수를 호출
document.addEventListener("DOMContentLoaded", main);

function main() {
  console.log(tag, "main");

  // storage 객체를 이용해서 store를 생성
  const store = new Store(storage);

  const views = {
    searchFormView: new SearchFormView(),
    searchResultView: new SearchResultView(),
    tabView: new TabView(),
    keywordListView: new KeywordListView(),
    historyListView: new HistoryListView(),
  };

    new Controller(store, views);
}
