import { TestBed } from '@angular/core/testing';

import { AppElementService } from './app-element.service';

describe('AppElementService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AppElementService = TestBed.get(AppElementService);
    expect(service).toBeTruthy();
  });
});
