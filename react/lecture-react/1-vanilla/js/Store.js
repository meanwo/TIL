import { TabType } from "./views/TabView.js";
import { createNextId } from "./helpers.js";

const tag = "[Store]";

export default class Store {
  // 여기서 stoarge는 MVC 패턴에서 모델의 역할을 함

  // Model : 데이터, 어플리케이션의 정보 등을 나타냄
  // View : 데이터 및 객체의 입력, 그리고 보여주는 출력부분을 담당
  // Controller : 사용자가 데이터를 클릭하고 수정하는 것에 대한 "이벤트"들을 처리하는 부분
  
  // constructor는 클래스의 생성자, storage라는 객체를 받음.
  constructor(storage) {
    console.log(tag, "constructor");

    if (!storage) throw "no storage";

    this.storage = storage;

    this.searchKeyword = "";
    this.searchResult = [];
    this.selectedTab = TabType.KEYWORD;
  }

  search(keyword) {
    this.searchKeyword = keyword;
    this.searchResult = this.storage.productData.filter((product) =>
      product.name.includes(keyword)
    );
    this.addHistory(keyword);
  }

  getKeywordList() {
    return this.storage.keywordData;
  }

  getHistoryList() {
    return this.storage.historyData.sort(this._sortHistory);
  }

  _sortHistory(history1, history2) {
    return history2.date > history1.date;
  }

  removeHistory(keyword) {
    this.storage.historyData = this.storage.historyData.filter(
      (history) => history.keyword !== keyword
    );
  }

  addHistory(keyword = "") {
    keyword = keyword.trim();
    if (!keyword) {
      return;
    }

    const hasHistory = this.storage.historyData.some(
      (history) => history.keyword === keyword
    );
    if (hasHistory) this.removeHistory(keyword);

    const id = createNextId(this.storage.historyData);
    const date = new Date();
    this.storage.historyData.push({ id, keyword, date });
    this.storage.historyData = this.storage.historyData.sort(this._sortHistory);
  }
}

